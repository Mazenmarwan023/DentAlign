import React, { useState, useRef } from 'react';
import styles from './DicomViewer.module.css';

export default function DicomViewer() {
    const [imageSrc, setImageSrc] = useState(null);
    const [fileName, setFileName] = useState('');
    const [zoom, setZoom] = useState(1);
    const [contrast, setContrast] = useState(100);
    const [brightness, setBrightness] = useState(100);
    const [rotation, setRotation] = useState(0);
    const fileInputRef = useRef(null);

    const handleFileUpload = (e) => {
        const file = e.target.files[0];
        if (file) {
            setFileName(file.name);
            const reader = new FileReader();
            reader.onload = (event) => {
                setImageSrc(event.target.result);
                setZoom(1);
                setContrast(100);
                setBrightness(100);
                setRotation(0);
            };
            reader.readAsDataURL(file);
        }
    };

    const handleZoomIn = () => setZoom((prev) => Math.min(prev + 0.2, 3));
    const handleZoomOut = () => setZoom((prev) => Math.max(prev - 0.2, 0.5));
    const handleRotate = () => setRotation((prev) => (prev + 90) % 360);
    const handleReset = () => {
        setZoom(1);
        setContrast(100);
        setBrightness(100);
        setRotation(0);
    };

    return (
        <div className={styles.container}>
            <header className={styles.header}>
                <div>
                    <h1 className={styles.title}>DICOM / Medical Imaging Viewer</h1>
                    <p className={styles.subtitle}>Interactive high-resolution medical DICOM and X-Ray viewer.</p>
                </div>

                <div className={styles.toolbar}>
                    <input 
                        type="file" 
                        ref={fileInputRef} 
                        accept="image/*,.dcm" 
                        onChange={handleFileUpload} 
                        className={styles.fileInput} 
                    />
                    <button 
                        className={styles.uploadBtn} 
                        onClick={() => fileInputRef.current && fileInputRef.current.click()}
                    >
                        📁 Load DICOM / Image
                    </button>

                    {imageSrc && (
                        <>
                            <button className={styles.toolBtn} onClick={handleZoomIn} title="Zoom In">🔍 +</button>
                            <button className={styles.toolBtn} onClick={handleZoomOut} title="Zoom Out">🔍 -</button>
                            <button className={styles.toolBtn} onClick={handleRotate} title="Rotate">🔄 Rotate</button>
                            <button className={styles.toolBtn} onClick={handleReset} title="Reset View">↺ Reset</button>
                        </>
                    )}
                </div>
            </header>

            {imageSrc && (
                <div className={styles.controlsBar}>
                    <label className={styles.sliderLabel}>
                        Contrast: {contrast}%
                        <input 
                            type="range" 
                            min="50" 
                            max="200" 
                            value={contrast} 
                            onChange={(e) => setContrast(e.target.value)} 
                        />
                    </label>
                    <label className={styles.sliderLabel}>
                        Brightness: {brightness}%
                        <input 
                            type="range" 
                            min="50" 
                            max="200" 
                            value={brightness} 
                            onChange={(e) => setBrightness(e.target.value)} 
                        />
                    </label>
                    <span className={styles.fileNameBadge}>{fileName}</span>
                </div>
            )}

            <div className={styles.viewportContainer}>
                {!imageSrc ? (
                    <div className={styles.placeholder} onClick={() => fileInputRef.current && fileInputRef.current.click()}>
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2" />
                            <circle cx="8.5" cy="8.5" r="1.5" />
                            <polyline points="21 15 16 10 5 21" />
                        </svg>
                        <p>No DICOM image loaded</p>
                        <span>Click here or use the Load button above to select a file</span>
                    </div>
                ) : (
                    <div className={styles.canvasArea}>
                        <img 
                            src={imageSrc} 
                            alt="DICOM View" 
                            className={styles.dicomImage}
                            style={{
                                transform: `scale(${zoom}) rotate(${rotation}deg)`,
                                filter: `contrast(${contrast}%) brightness(${brightness}%)`
                            }} 
                        />
                    </div>
                )}
            </div>
        </div>
    );
}

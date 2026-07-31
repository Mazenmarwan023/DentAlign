import React, { useState, useEffect } from 'react';
import styles from './StaffReports.module.css';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    PointElement,
    LineElement,
    ArcElement,
    Title,
    Tooltip,
    Legend
} from 'chart.js';
import { Bar, Pie, Line } from 'react-chartjs-2';

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    PointElement,
    LineElement,
    ArcElement,
    Title,
    Tooltip,
    Legend
);

export default function StaffReports() {
    const [stats, setStats] = useState({
        totalRevenue: 48500,
        monthlyAppointments: 142,
        activePatients: 389,
        completionRate: 94.2
    });

    // Chart 1 Data: Monthly Revenue Trend
    const revenueData = {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        datasets: [
            {
                label: 'Monthly Revenue ($)',
                data: [32000, 36500, 41000, 39000, 45000, 43000, 48500],
                backgroundColor: 'rgba(2, 132, 199, 0.75)',
                borderColor: '#0284c7',
                borderWidth: 2,
                borderRadius: 6,
            }
        ]
    };

    // Chart 2 Data: Appointment Status Distribution
    const appointmentStatusData = {
        labels: ['Completed', 'Confirmed', 'Scheduled', 'Cancelled'],
        datasets: [
            {
                data: [95, 28, 14, 5],
                backgroundColor: ['#10b981', '#3b82f6', '#f59e0b', '#ef4444'],
                hoverOffset: 4
            }
        ]
    };

    // Chart 3 Data: Patient Growth
    const patientGrowthData = {
        labels: ['Mar', 'Apr', 'May', 'Jun', 'Jul'],
        datasets: [
            {
                label: 'Total Active Patients',
                data: [290, 315, 340, 365, 389],
                borderColor: '#8b5cf6',
                backgroundColor: 'rgba(139, 92, 246, 0.15)',
                fill: true,
                tension: 0.3,
            }
        ]
    };

    return (
        <div className={styles.container}>
            <header className={styles.header}>
                <h1 className={styles.title}>Clinic Reports & Analytics</h1>
                <p className={styles.subtitle}>Overview of practice financial performance, appointment volumes, and patient demographics.</p>
            </header>

            {/* Metrics Overview Cards */}
            <div className={styles.metricsGrid}>
                <div className={styles.metricCard}>
                    <div className={styles.metricLabel}>Total Revenue (YTD)</div>
                    <div className={styles.metricValue}>${stats.totalRevenue.toLocaleString()}</div>
                    <div className={`${styles.metricSub} ${styles.positive}`}>+12.8% from last month</div>
                </div>

                <div className={styles.metricCard}>
                    <div className={styles.metricLabel}>Monthly Appointments</div>
                    <div className={styles.metricValue}>{stats.monthlyAppointments}</div>
                    <div className={`${styles.metricSub} ${styles.positive}`}>+8.4% volume</div>
                </div>

                <div className={styles.metricCard}>
                    <div className={styles.metricLabel}>Active Patients</div>
                    <div className={styles.metricValue}>{stats.activePatients}</div>
                    <div className={styles.metricSub}>Across 4 staff doctors</div>
                </div>

                <div className={styles.metricCard}>
                    <div className={styles.metricLabel}>Appointment Completion</div>
                    <div className={styles.metricValue}>{stats.completionRate}%</div>
                    <div className={`${styles.metricSub} ${styles.positive}`}>Low cancellation rate</div>
                </div>
            </div>

            {/* Charts Section */}
            <div className={styles.chartsGrid}>
                <div className={styles.chartCard}>
                    <h3 className={styles.chartTitle}>Revenue Performance</h3>
                    <div className={styles.chartWrapper}>
                        <Bar 
                            data={revenueData} 
                            options={{ responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } }} 
                        />
                    </div>
                </div>

                <div className={styles.chartCard}>
                    <h3 className={styles.chartTitle}>Appointment Status</h3>
                    <div className={styles.chartWrapper}>
                        <Pie 
                            data={appointmentStatusData} 
                            options={{ responsive: true, maintainAspectRatio: false }} 
                        />
                    </div>
                </div>

                <div className={`${styles.chartCard} ${styles.fullWidth}`}>
                    <h3 className={styles.chartTitle}>Patient Growth Trend</h3>
                    <div className={styles.chartWrapper}>
                        <Line 
                            data={patientGrowthData} 
                            options={{ responsive: true, maintainAspectRatio: false }} 
                        />
                    </div>
                </div>
            </div>
        </div>
    );
}

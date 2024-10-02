import numpy as np
import plotly.graph_objects as go
import streamlit as st
from scipy.special import hermite
from scipy.constants import hbar, pi

# Constants (you can modify these)
m = 1.0  # mass of the particle
omega = 1.0  # angular frequency
hbar = 1.0  # set to 1 for simplicity

# Define the wavefunction for the quantum harmonic oscillator
def psi_n(n, x, m, omega):
    # Hermite polynomial of order n
    Hn = hermite(n)
    
    # Define scaling parameters
    alpha = np.sqrt(m * omega / hbar)
    
    # Pre-factor normalization
    coeff = (1 / np.sqrt(2**n * np.math.factorial(n))) * (alpha / np.sqrt(np.pi))**0.5
    
    # Calculate wavefunction
    psi = coeff * np.exp(-alpha**2 * x**2 / 2) * Hn(alpha * x)
    
    return psi

# Plot wavefunction and probability amplitude
def plot_wavefunction_and_probability(n, x, psi_values):
    # Create a figure with two subplots (wavefunction and probability)
    fig = go.Figure()
    
    # Plot normalized wavefunction
    fig.add_trace(go.Scatter(x=x, y=psi_values, mode='lines', name=f'Wavefunction (n={n})'))
    
    # Plot probability amplitude (square of wavefunction)
    fig.add_trace(go.Scatter(x=x, y=psi_values**2, mode='lines', name=f'Probability Amplitude (n={n})'))
    
    # Update layout
    fig.update_layout(
        title=f'Quantum Harmonic Oscillator (n={n})',
        xaxis_title='Position (x)',
        yaxis_title='Wavefunction / Probability Amplitude',
        template='plotly_dark',
        height=600,
        legend_title="Legend"
    )
    
    return fig

# Streamlit app setup
st.title("Quantum Harmonic Oscillator Simulation")
st.write("""
This app simulates the normalized wavefunction and probability amplitude of 
a quantum harmonic oscillator for different energy levels. Use the slider 
to select the quantum number \(n\).
""")

# Slider input for quantum number n
n = st.slider("Select quantum number n", min_value=0, max_value=10, value=0)

# Define the x values (position)
x = np.linspace(-5, 5, 500)

# Calculate the wavefunction for the selected n
psi_values = psi_n(n, x, m, omega)

# Plot the wavefunction and probability amplitude
fig = plot_wavefunction_and_probability(n, x, psi_values)
st.plotly_chart(fig)


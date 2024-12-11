
# Eco Food Carbon Footprint Analysis

Eco Food is an innovative web application designed to address a critical environmental challenge: understanding and mitigating the carbon footprint of our meals. By leveraging cutting-edge AI technology, Eco Food empowers individuals to make informed choices that benefit both their health and the planet.

---

## Problem Statement

The global food system contributes significantly to greenhouse gas emissions, with food production, transportation, and preparation playing major roles. However, most people are unaware of the environmental impact of their meals and lack the tools to make sustainable choices. This lack of awareness perpetuates unsustainable practices, contributing to climate change and resource depletion.

---

## Solution

Eco Food provides an easy-to-use platform where users can:

1. Upload a food image to analyze its carbon footprint.
2. Receive actionable insights to reduce environmental impact.
3. Visualize the breakdown of emissions across production, transportation, and cooking stages.
4. Access sustainability tips to adopt eco-friendly habits.

By combining advanced AI models, interactive visualizations, and user-friendly design, Eco Food helps individuals understand and minimize their meal-related emissions.

---

## Features

1. **Carbon Footprint Analysis**: Analyze food images to estimate their environmental impact using advanced AI models.
2. **Interactive Visualizations**: Includes bar charts and pie charts to breakdown the carbon footprint.
3. **Sustainability Tips**: Provides actionable steps to reduce your carbon emissions.
4. **Engaging Animations**: Enhances user experience with Lottie animations.
5. **User-Friendly Interface**: Powered by Streamlit for seamless interaction.

---

## Installation and Setup

### Prerequisites

- Python 3.9 or later
- pip (Python package installer)
- A valid Google API Key for the Gemini model
- An `.env` file containing your Google API key:
  ```
  GOOGLE_API_KEY=your_api_key_here
  ```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PriyanshuDey23/EcoFoodAI.git
   
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open your web browser and navigate to `http://localhost:8501`.

---

## Usage

1. Upload a food image in `.jpg`, `.jpeg`, `jfif` or `.png` format.
2. Click the **Analyze Carbon Footprint** button to get a detailed breakdown of your meal's environmental impact.
3. View actionable sustainability tips to reduce your footprint.
4. Explore interactive visualizations for a deeper understanding of the carbon footprint breakdown.

---

## File Structure

```
EcoFood/
|-- EcoFoodAI/
|   |-- __init__.py
|   |-- prompt.py          # Contains the AI model prompt
|-- app.py                 # Main application script
|-- requirements.txt       # List of dependencies
|-- .env                   # Environment variables (not included in repo)
|-- README.md              # Documentation file
```

---

## Technologies Used

- **Programming Language**: Python
- **Web Framework**: Streamlit
- **AI Model**: Google Gemini 1.5 Flash
- **Visualization**: Plotly
- **Animations**: Streamlit-Lottie
- **Image Processing**: Pillow

---

## Requirements

See the [requirements.txt](requirements.txt) file for a full list of dependencies.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---




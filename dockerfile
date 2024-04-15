# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install git to clone the repository
RUN apt-get update && apt-get install -y git

# Clone the repository into the container at /app
RUN git clone https://github.com/edoob9/musicweb.git .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit listens on
EXPOSE 8501

# Command to run the Streamlit app when the container starts
CMD ["streamlit", "run", "your_app.py"]

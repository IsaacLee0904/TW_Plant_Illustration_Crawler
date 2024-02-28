FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system packages, create a new conda environment, install Python packages, and clean up in one RUN command to reduce image layers
RUN apt-get update && \
    apt-get install -y gcc g++ git && \
    rm -rf /var/lib/apt/lists/* && \
    conda create -n env python=3.8 -y && \
    echo "source activate env" > ~/.bashrc && \
    /bin/bash -c "source activate env && \
    pip install --upgrade pip && \
    pip install bs4==0.0.1 requests==2.25.1 scrapy==2.5.0 selenium==3.141.0 pandas fastapi uvicorn jinja2 httpx starlette" && \
    conda clean -afy

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run main.py when the container launches
CMD ["/bin/bash", "-c", "source activate env && uvicorn src.api.api:app --host 0.0.0.0 --reload"]


# Use SageMaker TensorFlow Python image as base
FROM 763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-training:2.14.1-cpu-py310-ubuntu20.04-sagemaker

# Install necessary packages like git and any others you may need
#RUN apt update && \
#    apt install -y --no-install-recommends <package> && \
#    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /opt/ml/processing

# Clone your GitHub repo (replace with your actual repository URL)
RUN git clone https://github.com/LeandroVidal555/ml-training-flow.git

# Set the working directory to the cloned repo
WORKDIR /opt/ml/processing/ml-training-flow

# Install any Python dependencies from your repo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# default Entry point: pull the latest version of the notebook, convert it, and run it 
#  (processing job creation will overwrite)
#CMD ["sh", "-c", "git pull && jupyter nbconvert --to script notebook.ipynb && python notebook.py"]
CMD ["sh", "-c", "git pull && jupyter nbconvert --to script notebook.ipynb && python training_flow/sgm_proc_job_docker/test_script.py"]

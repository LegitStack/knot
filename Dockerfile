FROM continuumio/anaconda3:latest as base

# manage path
ENV PATH /opt/conda/bin:$PATH
RUN echo "export PATH='/opt/conda/bin:$PATH'" > ~/.bashrc && \
    conda update -n base -c defaults conda

# make room for knot
RUN mkdir /app && \
    cd /app && \
    chmod -R 777 /app && \
    mkdir /app/knot && \
    cd /app/knot && \
    chmod -R 777 /app/knot

# install knot and requirements
ADD . /app
RUN pip install -r /app/requirements.txt && python /app/setup.py develop
WORKDIR /app/knot/web

# config jupyter lab to remove need for token
RUN jupyter lab --generate-config && \
    rm -f /root/.jupyter/juypter_notebook_config.py
COPY .docker/notebook/jupyter_notebook_config.py /root/.jupyter/

# install and enable jupyter notebook extensions
RUN conda install -y -c conda-forge jupyter_contrib_nbextensions && \
    jupyter contrib nbextension install --system

# install and enable jupyter notebook copy to clipboard functionality
RUN jupyter nbextension install --sys-prefix https://github.com/njwhite/jupyter-clipboard/archive/master.tar.gz && \
    jupyter nbextension enable --sys-prefix jupyter-clipboard-master/jupyter-clipboard/main


# fix shell situation
RUN rm -rf /bin/sh && \
    cp /bin/bash /bin/sh

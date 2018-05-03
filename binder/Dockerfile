FROM sagemath/sagemath:8.0

ENV NB_USER=sage
ENV HOME /home/sage

# Make sure the notebooks are in ${HOME}
COPY notebooks ${HOME}
USER root
RUN chown -R ${NB_USER}:${NB_USER} ${HOME}
USER ${NB_USER}

EXPOSE 8888
CMD ["jupyter", "notebook", "--notebook-dir=notebooks", "--ip", "'*'", "--port", "8888"]

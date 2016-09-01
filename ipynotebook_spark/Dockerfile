FROM centos:7
MAINTAINER data-sci team


RUN yum install -y epel-release
RUN yum -y update
RUN yum -y group install "Development Tools"
RUN yum -y install python-pip python-devel libffi-devel lapack-devel openssl-devel \
    libxslt-devel libxml2-devel libyaml-devel
RUN pip install --upgrade pip

#RUN rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
RUN yum -y install gcc gcc-c++ python-devel python-pip mysql-devel
RUN yum -y install libpng-devel.x86_64
RUN yum -y install freetype-devel.x86_64
RUN yum -y install lapack
RUN yum -y install lapack-devel.x86_64
RUN yum -y install python-devel.x86_64
RUN yum -y install mariadb
RUN yum -y install mariadb-devel.x86_64
RUN yum -y install maven


RUN pip install --upgrade pip
RUN pip install mistune
RUN pip install jsonschema
RUN pip install tornado
RUN pip install jinja2
RUN pip install pyzmq
RUN pip install -I ipython
RUN pip install ipython[notebook]
RUN pip install numpy
RUN pip install matplotlib
RUN pip install pandas
RUN pip install scipy
RUN pip install seaborn
RUN pip install MySQL-python
RUN pip install sqlalchemy
RUN pip install seaborn
RUN pip install python-statsd
RUN pip install scikit-learn
RUN pip install gevent
RUN pip install numpy
RUN pip install scipy
RUN pip install redis
RUN pip install hiredis
RUN pip install werkzeug
RUN pip install geoip2
RUN pip install cassandra-driver
RUN pip install nltk
RUN pip install lda
RUN pip install --user --install-option="--prefix=" -U scikit-learn
RUN pip install pyyaml ua-parser user-agents
RUN pip install vincent

# downdload nltk data
#RUN python -m nltk.downloader -d /usr/local/share/nltk_data all
#RUN python -m nltk.downloader -d /usr/local/share/nltk_data all
#RUN mkdir -p /usr/local/share/nltk_data
#RUN python -m nltk.downloader -d /usr/local/share/nltk_data -q wordnet
#RUN python -m nltk.downloader -d /usr/local/share/nltk_data -q snowball_data
#RUN python -m nltk.downloader -q wordnet
#RUN python -m nltk.downloader -q snowball_data

# download scala & spark
ENV SCALA_VERSION 2.10.6
ENV SPARK_VERSION 2.0.0
ENV CDH_VERSION cdh4
ENV SCALA_HOME /opt/scala-$SCALA_VERSION
ENV SPARK_HOME /opt/spark-$SPARK_VERSION
ENV PATH $SPARK_HOME/bin:$SCALA_HOME/bin:$PATH

ADD sw-gd-all.repo /etc/yum.repos.d/
ADD http://www.scala-lang.org/files/archive/scala-$SCALA_VERSION.tgz /
ADD http://apache.mirrors.hoobly.com/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop2.6.tgz /

RUN (cd / && gunzip < scala-$SCALA_VERSION.tgz)|(cd /opt && tar -xvf -)
RUN rm /scala-$SCALA_VERSION.tgz

RUN (cd / && gunzip < spark-$SPARK_VERSION-bin-hadoop2.6.tgz)|(cd /opt && tar -xvf -)
RUN rm /spark-$SPARK_VERSION-bin-hadoop2.6.tgz
RUN mv /opt/spark-$SPARK_VERSION-bin-hadoop2.6 /opt/spark-$SPARK_VERSION

RUN (cd /opt && ln -sf spark-$SPARK_VERSION spark)
RUN (cd /opt && ln -sf scala-$SPARK_VERSION scala)

# setup ipython notebook
RUN cd /opt && ln -sf spark-$SPARK_VERSION spark
RUN ipython profile create pyspark
RUN mkdir -p /root/.ipython/kernels/pyspark
ADD kernel.json /root/.ipython/kernels/pyspark/
ADD 00-pyspark-setup.py /root/.ipython/profile_pyspark/startup/
ADD ipython_notebook_config.py /root/.ipython/profile_pyspark/
ADD run_ipython.sh /root/

# create soft link - called data folder, shared with host
RUN (mkdir -p /data/ && ln -sf /data /root/data)

# setup tensorflow
ADD https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.8.0rc0-cp27-none-linux_x86_64.whl /
RUN easy_install --upgrade six
RUN pip install --upgrade tensorflow-0.8.0rc0-cp27-none-linux_x86_64.whl
RUN rm tensorflow-0.8.0rc0-cp27-none-linux_x86_64.whl


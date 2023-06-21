# we're using the latest master branch, which we previously build as dev build
FROM sg/auto-gpt:master AS atlas

# Unleash Start
# ssh key sorts github out
RUN ssh-keygen -q -t rsa -N '' -f /root/.ssh/id_rsa
RUN git config --global --add safe.directory /home/atlas

# if it wants to play with Rust, why not?
RUN curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh -s -- -y

### programming languages dependencies
RUN apt-get update \
    && apt-get install -y git curl libssl-dev libreadline-dev zlib1g-dev autoconf bison build-essential libyaml-dev libreadline-dev libncurses5-dev libffi-dev libgdbm-dev

# requirements2.txt is where to dump extra libraries that we get frequently stuck on
COPY ./requirements2.txt ./
RUN pip install --no-cache-dir -r requirements2.txt

# Ruby RVM install
RUN gpg --keyserver keyserver.ubuntu.com --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
RUN curl -L https://get.rvm.io | bash -s stable
ENV PATH /usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
RUN /bin/bash -l -c "echo 'source /usr/local/rvm/scripts/rvm' >> ~/.bashrc"
RUN /bin/bash -l -c "rvm requirements"
RUN /bin/bash -l -c "rvm install 3.2.1"
RUN /bin/bash -l -c "gem install bundler twurl"
RUN /bin/bash -l -c "echo 'source /usr/local/rvm/scripts/rvm' >> ~/.bashrc"
RUN /bin/bash -l -c "rvm use 3.2.1"

### This is where we add things that we see it get stuck on, frequently, if our mission is to make the exploratory road easier
RUN apt-get update \
    && apt-get install -y  apt-utils sudo git openssh-client sbcl cmake clisp unzip emacs man-db stockfish xz-utils zbarcam-gtk xvfb zbar-tools tesseract-ocr imagemagick strace eog vlc lynx

RUN apt-get update \
    && apt-get install -y rsync tree dnsutils

#WORKDIR /home/atlas
#RUN wget -O ./plugins/Auto-GPT-SystemInfo.zip https://github.com/hdkiller/Auto-GPT-SystemInfo/archive/refs/heads/master.zip 

# Unleash end

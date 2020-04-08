# Overview
gac is git account changer.  
This can change "git config --global user.{ name | email }" easily.

# Installation
```shell script
$ pip install git+https://github.com/satoooon8888/gac.git
```

# Usage
```shell script
$ gac add                        # add user setting
> user.name: john                (user input example)
> user.email: john@mail.com      (user input example)
$ gac set john                   # set git user config
$ git config --global user.email # test
> john@gmail.com
```
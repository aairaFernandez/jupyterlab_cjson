from setuptools import setup

setup_args = dict(
    name                 = 'jupyterlab_cjson',
    version              = '0.20.2',
    packages             = ['jupyterlab_cjson'],
    author               = 'Chris Harris',
    author_email         = 'chris.harris@kitware.com',
    url                  = 'http://jupyter.org',
    license              = 'BSD',
    platforms            = "Linux, Mac OS X, Windows",
    keywords             = [
        'ipython',
        'jupyter',
        'jupyterlab',
        'extension',
        'renderer'
    ],
    classifiers          = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires     = [
        'jupyterlab>=0.27.0',
        'notebook>=4.3.0',
        'ipython>=1.0.0'
    ]
)

if __name__ == '__main__':
    setup(**setup_args)

# The JupyterLab user interface
c.Spawner.default_url = '/lab'

# Jupyterhub Log level
c.JupyterHub.log_level = 'DEBUG'

# LDAP configurations
c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
c.LDAPAuthenticator.use_ssl = False
c.LDAPAuthenticator.server_address = '103.127.28.120'
c.LDAPAuthenticator.bind_dn_template = 'uid={username},cn=users,cn=accounts,dc=pdcloudex,dc=com'

# Admin Uesrs
c.Authenticator.admin_users = {'rajanikanth', 'ajay', 'anand', 'abhinish', 'deepak'}

# Whitelisted users
c.Authenticator.whitelist = {'rajanikanth', 'ajay', 'anand', 'abhinish', 'deepak', 'moses', 'srini', 'harish', 'sandeep', 'sohail', 'siman', 'priyag'}

# Spawner profiles
c.KubeSpawner.profile_list = [
    {
        'display_name': 'Minimal Notebook (Python 3.5)',
        'kubespawner_override': {
            'image_spec': 'minimal-nb:v7',
            'supplemental_gids': [100]
        }
    },
    {
        'display_name': 'Minimal Notebook (Python 3.6)',
        'default': True,
        'kubespawner_override': {
            'image_spec': 's2i-minimal-notebook:3.6',
            'supplemental_gids': [100]
        }
    },
    {
        'display_name': 'Jupyter - Scipy Notebook',
        'kubespawner_override': {
            'image_spec': 's2i-scipy-notebook:3.6',
            'supplemental_gids': [100]
        }
    },
    {
        'display_name': 'Iventura - Scipy Notebook',
        'kubespawner_override': {
            'image_spec': 'ajay2307/scipy:v7',
            'supplemental_gids': [100]
        }
    },
    {
        'display_name': 'Jupyter - Tensorflow Notebook',
        'kubespawner_override': {
            'image_spec': 's2i-tensorflow-notebook:3.6',
            'supplemental_gids': [100]
        }
    },
    {
        'display_name': 'Jupyter R-Notebook',
        'kubespawner_override': {
            'image_spec': 'r-notebook:v2',
            'supplemental_gids': [100]
        }
    }
]
c.KubeSpawner.supplemental_gids = [100]

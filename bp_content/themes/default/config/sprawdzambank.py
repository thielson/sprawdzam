config = {

    # This config file is used only in appengine.beecoss.com (Sample website)
    # Don't use values defined here
    'environment': "sprawdzambank",

    # contact page email settings
    'contact_sender': "thielson@gmail.com",
    'contact_recipient': "thielson@gmail.com",

    'send_mail_developer': False,

    # fellas' list
    'developers': (
        ('Thielson', 'thielson@interia.pl'),
    ),

    # It is just an example to fill out this value
    'google_analytics_code': """
            <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-62889832-1', 'auto');
  ga('send', 'pageview');

</script>
        """,

    # Password AES Encryption Parameters
    # aes_key must be only 16 (*AES-128*), 24 (*AES-192*), or 32 (*AES-256*) bytes (characters) long.
    'aes_key': "33ac8be719b29c20f3bb8a130bb576a4",
    'salt': "dbkETeF$<^>%%X^8|e[9td62`dobFL[V&F&**@`UP6vqjGL,>v+k@ma^zd6WdG0;H>o-SGG9ynkR",

    # get your own consumer key and consumer secret by registering at https://dev.twitter.com/apps
    # callback url must be: http://[YOUR DOMAIN]/login/twitter/complete
    'twitter_consumer_key': 'n2fKahqt4L1NZj8V2AhSAZNuS',
    'twitter_consumer_secret': 'p9w2bieS8LqvMWQCMphz2HCiCrdtFg0DVMa9tNUSgCoKHCr5QT',

    #Facebook Login
    # get your own consumer key and consumer secret by registering at https://developers.facebook.com/apps
    #Very Important: set the site_url= your domain in the application settings in the facebook app settings page
    # callback url must be: http://[YOUR DOMAIN]/login/facebook/complete
    'fb_api_key': '678338665605528',
    'fb_secret': 'bd5b7a0165fbd0e3fe97b067e2d715fe',

    #Linkedin Login
    #Get you own api key and secret from https://www.linkedin.com/secure/developer
    'linkedin_api': 'ueNRJIsyU3Q_EXer9MTOT3fpH-rQCGZWBBhVCeV3gyDzgNSB9Ov04DM3j6WEpSHf',
    'linkedin_secret': 'NYgmelU0_7PKf0LXYNq8ujtrp0F9UWBKaxd1hQOoBwiwVecHyZB9uTihZ-y7g4Me',

    # Github login
    # Register apps here: https://github.com/settings/applications/new
    'github_server': 'github.com',
    'github_redirect_uri': 'http://appengine.beecoss.com/social_login/github/complete',
    'github_client_id': 'c391bcae77f69499bb46',
    'github_client_secret': '00674550b11a7644e675129a4ddbdaa2798addae',

    # get your own recaptcha keys by registering at http://www.google.com/recaptcha/
    'captcha_public_key': "6Ldi0u4SAAAAAC8pjDop1aDdmeiVrUOU2M4i23tT",
    'captcha_private_key': "6Ldi0u4SAAAAAPzk1gaFDRQgry7XW4VBvNCqCHuJ",

    # webapp2 sessions
    'webapp2_extras.sessions': { 'secret_key': 'coto#W1|(|=_>}m9BZEB#drBG| tN@0{@7+)gB:w:+9u3}nlrf8U?' },

    # webapp2 authentication
    'webapp2_extras.auth': { 'cookie_name': 'gae_session' },

    # ----> ADD MORE CONFIGURATION OPTIONS HERE <----

}
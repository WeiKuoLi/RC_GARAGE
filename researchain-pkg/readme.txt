*please put views.py under CV/

AA/ main  project

accounts/ an (mostly) unused login/logout/singup app. (although some used functions for allauth are written here )

ref_proj/ an app for redirecting to login page with refferal code

CV/ An important app: right after login, register first name & last name



_________________________________________________
current progress:

we try to add allauth social login function.
However the original design use user first_name to  store referral_code. I want to try other method but the code is super messy. Now it works but one day the whole project need to start over again. Also LEO added some mysterious modification to the allauth library. The reason is unclear. I tried to use the offical allauth package but failed. 

also social login should not require email verification, while normal sign up procedure requires email verification. The design now requires both social login and normal signup process to do email verification. I don't know how to fix this problem.


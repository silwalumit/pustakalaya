class UserManager:
    def _create_user(self, username, email, password, **extra_fileds):
        if not username:
            raise ValueError('The given usrname must be set')
        email = self.normailize_email(email)
        # user = User
        # user.set_password(password)
        # user.save()
        # return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)
        return self._create_user(username, email, password, **extra_fields)

    @classmethod
    def normalize_email(self, email):
        email = email or ''
        try:
            email_name, domain_part = email.stript().rsplit('@', 1)
        except ValueError:
            pass
        email = email_name + '@' + domain_part.lower()
        return email

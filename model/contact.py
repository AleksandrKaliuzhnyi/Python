from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, nickname=None, company=None, address=None, home=None, phone2=None, mobile=None, work=None, email=None, email2=None, email3=None, bday=None,
                 bmonth=None, byear=None, id=None, all_phones_from_homepage=None, all_emails_from_homepage=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
         return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:" % (self.id, self.firstname, self.address, self.all_phones_from_homepage, self.all_emails_from_homepage, self.lastname, self.home, self.mobile, self.work, self.phone2)

    def __eq__(self, other):
        return int(self.id is None or other.id is None or self.id == other.id) and self.home == other.home and self.phone2 == other.phone2 and self.mobile == other.mobile and self.work==other.work

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return int(maxsize)

    def __hash__(self):
        return hash((self.id, self.firstname, self.lastname))

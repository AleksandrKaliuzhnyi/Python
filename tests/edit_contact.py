from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login( username="admin", password="secret")
    app.contact.edit_first_contact(Contact("Alex", "Last", "Last", "Infopulse", "Kharkiv", "0931234561", "AQA",
                            "1test@gmail.com", "5", "June", "1993"))
    app.session.logout()

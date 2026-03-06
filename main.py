from pyscript import document

def account_creation(e):
    out = document.getElementById('output')
    email = document.getElementById('email').value
    user = document.getElementById('username').value
    pw = document.getElementById('password').value
    if not email.endswith("@obmontessori.edu.ph"):
        out.innerHTML = "<span style='color:red'>⚠️ School domain only</span>"
    elif len(user) < 7:
        out.innerHTML = "<span style='color:red'>⚠️ Username: 7 chars min</span>"
    elif len(pw) < 10 or not any(c.isdigit() for c in pw) or not any(c.isalpha() for c in pw):
        out.innerHTML = "<span style='color:red'>⚠️ Password: 10 chars, letter + number</span>"
    else:
        out.innerHTML = "<span style='color:#00ff00'>✅ Account Ready!</span>"
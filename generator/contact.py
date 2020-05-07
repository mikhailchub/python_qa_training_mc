from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print
    str(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*5
    return prefix \
           + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" \
           + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + ".com"


def random_phone(prefix, maxlen):
    symbols = string.digits*100 + string.ascii_letters + string.punctuation + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("First ", 10), lastname=random_string("Last ", 10),
            address=random_string("Address ", 30),
            email=random_email("email", 5), email2=random_email("email", 5), email3=random_email("email", 5),
            homephone=random_phone("+", 15), mobilephone=random_phone("+", 15), workphone=random_phone("+", 15),
            secondaryphone=random_phone("+", 15))
    for firstname in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

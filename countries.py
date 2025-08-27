class india ():
    def capital(self):
        print("New Delhi is the capital of india")
    def language(self):
        print("hindi is the most widly spoken language in india")
    def type (self):
        print("india is a developing country")
class USA ():
    def capital(self):
        print("Washington DC is the capital of USA")
    def language(self):
        print("english is the most widly spoken language in USA")
    def type (self):
        print("USA is a developed country")
i = india()
u = USA()
for country in(i,u):
    country.capital()
    country.language()
    country.type()
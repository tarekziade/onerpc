from onerpc import Service, locate_service

# init..
locate_service('science', 'tcp://0.0.0.0:1234')


# the app...
science_service = Service('science')
print science_service.multiplication(3, 5)




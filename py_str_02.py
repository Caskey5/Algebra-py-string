first_name = input('Unesite svoje ime: ')
last_name = input('Unesite svoje prezime: ')

# message = 'Dobro dosli' + first_name + ' ' + last_name + '.'
message = 'Dobro dosli {} {}.'.format(first_name, last_name)
# message = f'Dobro dosli {first_name} {last_name}'

print(message)
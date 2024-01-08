
class patient:
    hospital_name = 'abc hospital'
    location = 'chennai'
    list1 = []

    def __init__(self, name, phone, appointment):
        self.name = name
        self.phone = phone
        self.appointment = appointment

    @classmethod
    def hospital(cls):
        print('\n-----hospital records-----')
        print(f'Hospital name: {cls.hospital_name}')
        print(f'Hospital location: {cls.location}')

    def patient_info(self):
        print(f'\nPatient name: {self.name}')
        print(f'Patient phone number: {self.phone}')
        print(f'{self.name} appointment time: {self.appointment}\n')
        print('register successfully')

    @classmethod
    def call(cls):
        while True:
            name = input('\nEnter your name: ')
            if len(name)<=2:
                print('\nname must contain more than 2 characters')
                continue
            phone = int(input('Enter your number: '))
            if phone<10:
                print('\n invalid phone number please enter your 10 digit phone number')
                continue
            appointment = input('Enter your appointment(AM/PM):   ')
            patient1 = patient(name, phone, appointment)
            cls.list1.append(patient1)

            choice = input('Enter 1 to see your details [press q to exit]: ')
            if choice == '1':
                patient1.patient_info()
                
            elif  choice.lower()=='q':
                break

    @classmethod
    def display_list(cls):
        print("\nPatient List For Today Appointment:\n")
        for i in cls.list1:
            print(f'Patient Name: {i.name}')
            print(f'Phone: {i.phone}')
            print(f'Time For Appointment: {i.appointment}\n')



patient.call()

patient.hospital()
patient.display_list()

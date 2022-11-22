from aplication.salary import calculate_salary
from aplication.db import people
#################
import vk_api
#################
if __name__ == '__main__':

    calculate_salary()
    people.get_employees()

###########################################################################
vk_session = vk_api.VkApi('+71234567890', 'mypassword')
vk_session.auth()

vk = vk_session.get_api()

print(vk.wall.post(message='Hello world!'))
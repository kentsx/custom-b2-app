from tinydb import TinyDB, Query
import os


class db_ops:

    def __init__(self) -> None:
        self.BAES_DIR = os.getcwd()
        db_name = 'UserDB'
        self.db_dir = os.path.join(self.BAES_DIR, 'GUI', '%s.json') % db_name
        self.db = TinyDB(self.db_dir)

    def initiate(self):
        # self.db = TinyDB(self.db_dir)
        self.db.drop_tables()

    def add_user(self, account, key_id, app_key, endpoint, custom_url):
        Unique = Query()   # 防止重复数据
        if account and key_id and app_key and endpoint and custom_url:
            is_unique = self.db.search((Unique.account == account) | (
                Unique.key_id == key_id) | (Unique.app_key == app_key))
            if not is_unique:
                # print('数据不重复')
                user_info = {
                    'account': account,
                    'key_id': key_id,
                    'app_key': app_key,
                    'endpoint': endpoint,
                    'custom_url': custom_url
                }
                self.db.insert(user_info)
            else:
                raise ValueError('输入数据重复')
        else:
            raise ValueError('数据为空')
            # raise

    def query_info(self, *args):
        User_query = Query()
        if args:
            query_list = self.db.search(User_query.account == args[0])
            # print(query_list)
        else:
            query_list = self.db.all()
        # print(li)
        # print(query_list)
        return query_list

    def query_users(self, *args):
        # User_query = Query()
        # if args:
        #     query_list = self.db.search(User_query.account == args[0])
        #     # print(query_list)
        # else:
        #     query_list = self.db.all()
        query_list = self.query_info(*args)
        # print(li)
        user_list = []
        for i in query_list:
            user_list.append(i['account'])
        # print(user_list)
        return user_list

    # def write_to_credentials(self):
    #     with open('credentials.py', 'r') as f:
    #         f.readlines()


if __name__ == '__main__':
    db = db_ops()
    # db.write_to_credentials()
    db.initiate()
    # db.add_user('kent3', '123456332123', 'ufafjasfj231kaljf21')
    # x = db.query_users()
    # if x:
    #     print('有数据')
    # else:
    #     print('空')

 
from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)
 
# mongodb 配置
app.config['MONGO_URI'] =  "mongodb+srv://{user_name}:{pass_word}@{host{port}/{database}".format(
        user_name='haor',
        pass_word='lhr368519',
        host='cluster0.hirzqvu.mongodb.net/myFirstDatabase',
        port=27017,
        database='Cluster0'
    )
mongo = PyMongo(app)
 
 
# 查找
def get_form_mongo_find(collection_name, conditions_dic, order_rule="", page_num=1, page_size=10):
    """
    按条件查询mongo，支持字段筛选、排序、分页、
    collection_name : 表名
    # 筛选条件
    conditions_dic : {'_id': ObjectId('5e4557da1ab80155d1ef3741')} - {'name': 'value'}
        in  操作: {'_id': {'$in': []}}
        大于等于: {"create_time": {"$gte": start_time}}  # 大于，$lt:小于，$gte:大于或等于，$lte:小于或等于
    # 排序规则
    order_rule : ("order_field", -1)
    """
    mycol = mongo.db[collection_name]
    if order_rule:
        table_info_list = mycol.find(conditions_dic).sort([order_rule]).skip(page_num*(page_num-1)).limit(page_size)
    else:
        table_info_list = mycol.find(conditions_dic).skip(page_num * (page_num - 1)).limit(page_size)
    count = mycol.find(conditions_dic).count()
    return table_info_list, count
 
 
# 更新
def update_mongo_info(collection_name, conditions_dic,  data_dic, multi_field_update=False):
    """
    修改
    collection_name: 表名
    conditions_dic: 筛选条件字典
    data_dic: 修改数据字典
    multi_field_update:  True-多字端修改 or False-单字段修改
    """
    mycol = mongo.db[collection_name]
    mycol.update(conditions_dic, {'$set': data_dic}, multi=multi_field_update)
    return
 
 
# 获取单条数据
def get_find_one(collection_name,  conditions_dic):
    """
    collection_name: 表名
    conditions_dic: 筛选条件字典
    """
    mycol = mongo.db[collection_name]
    info = mycol.find_one(conditions_dic)
    return info
 
 
def get_data_from_mongo_by_id(collection_name, condition_dic):
    """
    collection_name： 表名 - str
    condition_dic： 检索条件 - dict
    """
    mycol = mongo.db[collection_name]
    res = mycol.find(condition_dic)
    return res
 
 
def update_mongo_info_one_field(collection_name, conditions_dic,  data_dic):
    """
        单字段修改数据
        collection_name: 表名字符串
        conditions_dic: 筛选条件字典
        data_dic: 修改数据字典
    """
    mycol = mongo.db[collection_name]
    mycol.update(conditions_dic, {'$set': data_dic})
 
 
def add_data_to_mongo(collection_name, data_dic):
    """
        单字段修改数据
        collection_name: 表名字符串
        data_dic: 数据字典
    """
    mycol = mongo.db[collection_name]
    mycol.insert(data_dic)
 
 
@app.route('/')
def hello_world():
    add_data_to_mongo('User', {'username': "aaa"})
    return 'Hello World!'
 
 
if __name__ == '__main__':
    app.run()
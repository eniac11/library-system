from xml.etree import ElementTree as et

ns = {
    'xsd': 'http://www.w3.org/2001/XMLSchema',
    'od': 'urn:schemas-microsoft-com:officedata'
}


def get_ns_name(namspace, name):
    return "{" + ns[namspace] + "}" + name


affinities = {
    'INTEGER': [
        'INT',
        'INTEGER',
        'TINYINT',
        'SMALLINT',
        'MEDIUMINT',
        'BIGINT',
        'UNSIGNED BIG INT',
        'INT2',
        'INT8'
    ],
    'TEXT': [
        'CHARACTER(20)',
        'VARCHAR', # (255)
        'VARYING CHARACTER', # (255)
        'NCHAR', # (55)
        'NATIVE CHARACTER', # (70)
        'NVARCHAR', # (100)
        'TEXT',
        'NTEXT',
        'CLOB'
    ],
    'NONE': ['BLOB'],
    'REAL': [
        'REAL',
        'DOUBLE',
        'DOUBLE PRECISION',
        'FLOAT'
    ],
    'NUMERIC': [
        'NUMERIC',
        'DECIMAL', # (10,5)
        'BOOLEAN',
        'BIT',
        'DATE',
        'DATETIME'
    ]
}

def get_affinity(ttype: str):
    for key, val in affinities.items():
        if ttype.upper() in val:

            return key



db = et.parse("Books.xml")

xsd = et.parse("Books.xsd")
dataroot = db.getroot()
db.write("Books_pretty.xml")
xsd_root = xsd.getroot()
# print(xsd_root[1][0][0][1].attrib['index-name'])
# for field in xsd_root[1][0][0]:
#     if 'index-name' in field.attrib:
#         print(field.attrib)

seq = xsd_root[1][1][0]

# print(xsd_root[1][0][0].tag)


datatypes = {}

for field in seq:
    sql_type = None
    if not 'type' in field.attrib.keys():
        
        sql_type = get_affinity(field.attrib[get_ns_name("od", "sqlSType")])
    else:
        sql_type = get_affinity(field.attrib['type'].split(':')[1])
    name = field.attrib["name"]
    datatypes[name] = {}
    datatypes[name]["type"] = sql_type
    # Primary
    # Unique
    if len(field) == 2:
        datatypes[name]["max_length"] = field[1][0][0].attrib["value"]
    # else:
    #     datatypes[name]['max_length'] = None


def yes_or_no(obj):
    if obj == "yes":
        return True
    else:
        return False

# print(datatypes)

for structure in xsd_root[1][0][0]:
    if structure.tag == get_ns_name("od", "index"):
        index_key = structure.attrib["index-key"]
        primary = yes_or_no(structure.attrib['primary'])
        unique= yes_or_no(structure.attrib['unique'])
        clustered= yes_or_no(structure.attrib['clustered'])
        order=yes_or_no(structure.attrib['order'])
        data = {
            'index-key': index_key,
            'primary': primary,
            'unique': unique,
            'clustered': clustered,
            'order': order
            }
        datatypes[index_key[0:-1]].update(data)

# for key, val in datatypes.items():
#     print(key, val)
        
def text_col(key, data):
    return data['type'] + '(' + data['max_length'] + ')'

def int_col(key, data):
    return data['type']

def real_col(key, data):
    return data['type']

def numeric_col(key, data):
    return data['type']
        
def generate_column(name, data):
    col = ""
    # if "_x0020_" in key:
    col = '"' + key.replace("_x0020_", " ") + '" ' 
    # else:
    #     col = key + ' '
    dtype = data['type']
    if dtype == 'TEXT':
        col+= text_col(key, val)
    elif dtype == 'INTEGER':
        col += int_col(key, data)
    elif dtype == 'NONE':
        col += 'None'
    elif dtype == 'REAL':
        col += real_col(key, val)
    elif dtype == 'NUMERIC':
        col += numeric_col(key, val)
    return col

book = dataroot[0]
len_book = len(datatypes.keys())
print("'''CREATE TABLE books (", end="")

counter = 0
# for book in dataroot:
for key, val in datatypes.items():

    if counter != len_book -1:

        print(generate_column(key, val), end=", ")
        
    else:
        print(generate_column(key, val), end="")
    counter += 1
print(")", end="'''")

print()


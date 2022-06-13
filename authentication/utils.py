import json, string, urllib, urllib.request, calendar, datetime, random, re


class functions:
    def add_months(self, sourcedate, months):
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        day = min(sourcedate.day, calendar.monthrange(year, month)[1])
        return datetime.date(year, month, day)

    def deleter(self, table, condition=''):
        conn = self.connect()
        try:
            sql = "DELETE FROM {} {}".format(table, condition)
            print(sql)
            with conn.cursor() as con:
                con.execute(sql)
                conn.commit()
                msg = 'ok'
        except Exception as err:
            msg = err
            print(err)
        finally:
            conn.close()
        return msg

    def updater(self, table, update, where=''):
        conn = self.connect()
        try:
            sql = "UPDATE {} SET {} {}".format(table, update, where)
            print(sql)
            with conn.cursor() as con:
                con.execute(sql)
                conn.commit()
                msg = 'ok'
        except Exception as err:
            msg = err
            print(err)
        finally:
            conn.close()
        return msg

    def seckey(self, a, b):
        rand = random.randint(a, b)
        return rand

    def sanitizeString(self, input):
        whiteList = string.ascii_letters + string.digits + " !?$.,;:-'()&"
        filters = filter(lambda x: x in whiteList, input)
        return filters

    def replacer(self, replacer, replacee, sentence):
        sentence = sentence.strip()
        return sentence.replace(replacer, replacee)

    def htmlEn(self, input):
        if "<" in input or ">" in input:
            message = input.replace("<", "&lt;")
            message = message.replace(">", "&gt;")
            both = message
        else:
            both = input
        return both

    def htmlDe(self, input):
        if "&lt;" in input or "&gt;" in input:
            message = input.replace("&lt;", "<")
            message = message.replace("&gt;", ">")
            both = message
        else:
            both = input
        return both

    def password(self, password):
        password = hash.apr_md5_crypt.encrypt(password)
        return password

    def verify(self, password, dbpass):
        newpass = str(password)
        return hash.apr_md5_crypt.verify(newpass, dbpass)

    def inpck(self, data):
        if data:
            return self.htmlEn(data.strip())
        # elif not data.strip():
        #     return False

    def lowerInpck(self, data):
        if data:
            data = data.strip()
            return data.lower()

    def empty(self, vars):
        for items in vars:
            if not items:
                return True

    def formatDateTime(self, value):
        if type(value) == 'str':
            day = datetime.datetime.strptime(value, '%d/%m/%y')
            time = datetime.datetime.strptime(value, '%H:%M:%S')
        else:
            day = value.strftime("%Y-%m-%d")
            time = value.strftime("%H:%M:%S")
        result = [day, time]
        return result

    def calculateAge(self, birthDate):
        if type(birthDate) == str:
            birthDate = datetime.datetime.strptime(birthDate, "%Y-%m-%d")
        today = datetime.date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        return age

    def emptyValue(self, value):
        if value is None:
            value = ''
        return value

    def numbComma(self, val):
        if val is None:
            val = 0
        return "{:,}".format(val)

    def myfilter(self, myList):
        unique_list = []
        for x in myList:
            if x not in unique_list:
                unique_list.append(x)
        return unique_list

    def typeOf(self, value):
        return type(value)

    def telValidate(self, data):
        if data:
            if not data.isdigit():
                return "Only Numbers allowed. Remove '+'"
            elif len(data) != 11:
                if len(data) != 13:
                    return "11 Digits Allowed. 234 Allowed Too"
                else:
                    return 'ok'
            else:
                return 'ok'

    def username(self, data):
        if data:
            data = data.lower()
            data = data.strip()
            username = False
            if " " not in data:
                username = True
            return username

    def emailCheck(self, data):
        if data:
            email = False
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', data)
            if match != None:
                email = True
            return email


    def python_to_json(self, data):
        try:
            return json.dumps(data)
        except Exception as err:
            print(err)
            return err

    def mylist(self, data):
        newarray = []
        for item in data:
            item = item.__str__()
            newarray.append(item)
        # print(f"new is: {newarray}")
        return json.dumps(newarray)

    def printArray(self, array):
        resp = 'Response is: '
        for item in array:
            resp += f"{item}, "
        return resp

    def printForm(self, form):
        resp = "<center><b>Form elements:</b></center><br> "
        for item in form:
            resp += f"{item} = {form[item]} <br>"
        return resp

    def json_to_python(self, data):
        try:
            return json.loads(data)
        except Exception as err:
            print(err)
            return err

    def gen_string(self, size=7, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def fulldate(self):
        current_ = datetime.datetime.now()
        day = current_.strftime("%A")
        date = current_.strftime("%d")
        month = current_.strftime("%b")
        year = current_.strftime("%Y")
        msg = f"{day}, {month} {date} {year}"
        return msg

    def getYear(self):
        current_ = datetime.datetime.now()
        return current_.strftime("%Y")

    def greetings(self):
        current_ = datetime.datetime.now()
        current_hour = current_.hour
        if current_hour == 0 or current_hour <= 11:
            msg = "Good Morning"
        elif current_hour <= 16:
            msg = "Good Afternoon"
        else:
            msg = "Good Evening"
        return msg

    def total(self, one, two):
        if one is None:
            one = 0
        if two is None:
            two = 0
        result = one + two
        return "{:.2f}".format(result)

    def namestr(self, obj, namespace):
        return [name for name in namespace if namespace[name] is obj]

    def checkImportant(self, Arrays):
        msg = ''
        for x in Arrays:
            if self.inpck(x) == '':
                VAR = self.namestr(x, globals())
                msg += f"<br>{VAR} is Empty"
        return msg

from datetime import timezone, timedelta
from passlib.hash import pbkdf2_sha256


class Utils():

    def __init__(self):
    pass

    @ classmethod
    def timestamp(cls, dt):
        return dt.replace(tzinfo=timezone.utc).timestamp() * 1000

    @ classmethod
    def time_range(self, start, diff, curr):
        """
            Function to find if a datetime object {curr} is within the minute ranges {diff} of another datetime object in milliseconds
        """
        td = timedelta(minutes=diff)
        end = start + td
        
        start = self.timestamp(start)
        end = self.timestamp(end)

        return bool(start <= curr <= end)

    @ classmethod
    def generate_order_id(cls, db):

        minimum = pow(4, 5-1)
        maximum = pow(4, 5) - 1

        cond = False
        while cond is False:
            var1 = random.randint(minimum, maximum)
            var2 = db.get_by_ordernum(order_id=var1)
            print(var2)

            if var2 is None:
                cond = True
            else:
                pass
        return var1

    @ classmethod
    def hash_password(cls, password):
        return pbkdf2_sha256.hash(password)

    @ classmethod
    def check_password(cls, password, hashed):
        return pbkdf2_sha256.verify(password, hashed)

import requests
import hashlib
import sys

def request_api(query_char):
    url="https://api.pwnedpasswords.com/range/"+query_char
    res=requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f"Error fetching :{res.status_code}")
    return res
def get_password(hashes,hashcheck):
    hashes=(line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
         if h == hashcheck:
               return count
    return 0



def pwned_api_check(password):
    sha1p=hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
    first5,tail=sha1p[:5],sha1p[5:]
    response= request_api(first5)
    print(response)
    return get_password(response,tail)

def main(args):
    for password in args:
        count=pwned_api_check(password)
        if count:
            print(f"password found {count} times")
        else:
            print("password safe")
    return "done"
main(sys.argv[1:])
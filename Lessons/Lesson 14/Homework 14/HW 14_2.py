# Task 2
# Write a decorator that takes a list of stop words and replaces them with *inside the decorated function  ```

def stop_words(words: list):
    def stop_words_dec(f):
        def wrapper(name):
            result = f(name).split('!')
            new_result = []
            res2 = result[0].split()
            # print(res2)
            for i in res2:
                if i in words:
                    new_result.append('*')
                else:
                    new_result.append(i)

            for i in new_result:
                print(i,end=' ')
            print('!')
        return wrapper
    return stop_words_dec

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

create_slogan("Steve")

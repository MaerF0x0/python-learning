
# Examples of ways to define function args

def simple(x, y, z):
    print(f'{x}, {y}, {z}')


def defaults(x, y=None):
    print(f'{x}, {y}')

def arbitary_num_args(x, *args):
    print(f'{x}, {args.count}') 

def arbitrary_kw_args(x, **kwargs): 
     print(f'{x}, {kwargs.keys}')

def invoke_with_named_args():
    # note how the order is different
    simple(z=2, y=3, x=12)

def with_type_hinting(name: str, cash:float, number_of_friends:int, is_happy: bool, memes: list, resume: dict, tupleee: tuple[int, float]):
    pass

with_type_hinting("mike", 1000, 20, True, ['side_eye_cloe'], {'Twilio':'2018-2023'}, (12, 12.0))

def with_return_type() -> bool:
    return "mike"

    
print(with_return_type())
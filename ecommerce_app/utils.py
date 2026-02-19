import copy

class CartUtils:
    @staticmethod
    def demonstrate_copy_logic(cart_data):
        """Demonstrate shallow vs deep copy (Advanced Python Concept)"""
        shallow = copy.copy(cart_data)
        deep = copy.deepcopy(cart_data)
        return shallow, deep

def generator_pagination(queryset, page_size):
    """Generator-based pagination for efficient memory usage"""
    for i in range(0, len(queryset), page_size):
        yield queryset[i:i + page_size]

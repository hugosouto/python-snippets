from even_numbers_generator_function import return_evens

def test_return_evens():
    try:
        # Test case 1: Test with an empty list
        assert list(return_evens([])) == []

        # Test case 2: Test with a list of odd numbers
        assert list(return_evens([1, 3, 5, 7, 9])) == []

        # Test case 3: Test with a list of even numbers
        assert list(return_evens([2, 4, 6, 8, 10])) == [2, 4, 6, 8, 10]

        # Test case 4: Test with a list of mixed numbers
        assert list(return_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [2, 4, 6, 8, 10]

        # Test case 5: Test with a list of negative even numbers
        assert list(return_evens([-4, -6, -8, -10])) == [-4, -6, -8, -10]

        # Test case 6: Test with a list of negative odd numbers
        assert list(return_evens([-3, -5, -7, -9])) == []

        # Test case 7: Test with a list of one even number
        assert list(return_evens([2])) == [2]

        # Test case 8: Test with a list of one odd number
        assert list(return_evens([3])) == []

        # Test case 9: Test with a list of repeated even numbers
        assert list(return_evens([2, 2, 2, 2, 2])) == [2, 2, 2, 2, 2]

        # Test case 10: Test with a list of repeated odd numbers
        assert list(return_evens([3, 3, 3, 3, 3])) == []

        # Test case 11: Test with a list of mixed numbers including zero
        assert list(return_evens([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [0, 2, 4, 6, 8, 10]

        # Test case 12: Test with a list of mixed numbers including negative zero
        assert list(return_evens([-0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [0, 2, 4, 6, 8, 10]

        # Test case 13: Test with a list of mixed numbers including floating point numbers
        assert list(return_evens([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])) == [2.0, 4.0, 6.0, 8.0, 10.0]

        # Test case 14: Test with a list of mixed numbers including negative floating point numbers
        assert list(return_evens([-1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0, -8.0, -9.0, -10.0])) == [-2.0, -4.0, -6.0, -8.0, -10.0]
        
        print("Success: All tests passed!")
    
    except AssertionError:
        print("Failure: One or more tests failed.")

if __name__ == "__main__":
    test_return_evens()
def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

##START
import random

class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        result = [] #empty array
        return result

class TestDataUniqueValues(object):
    result = set()
    while len(result) < 10:
        result.add(random.randint(0,100))
    @staticmethod
    def get_array():
        # array of size at least 2 with all unique elements
        result = TestDataUniqueValues.result
        return list(result)

    @staticmethod
    def get_expected_result():
        # return the expected minimum value index for this array
        result = TestDataUniqueValues.get_array()
        return result.index(min(result))

class TestDataExactlyTwoDifferentMinimums(object):
    result = set()
    while len(result) < 10:
        result.add(random.randint(0,100))
    result = list(result)
    result.append(min(result))
    @staticmethod
    def get_array():
        # return an array where there are exactly two different minimum values
        result = TestDataExactlyTwoDifferentMinimums.result
        return result
    @staticmethod
    def get_expected_result():
        # return the expected minimum value index for this array
        result = TestDataExactlyTwoDifferentMinimums.get_array()
        return result.index(min(result))

##FINISH

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")


import csv
import logging
import argparse
parser = argparse.ArgumentParser(description='Student parser')
parser.add_argument('name', type=str, help='Type the name of student')
parser.add_argument('last_name', type=str, help='Type the surname of student')
args = parser.parse_args()


logging.basicConfig(level=logging.INFO, filename='student_log.log', filemode='w')


class CheckName:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value.istitle() and value.isalpha():
            setattr(instance, self.param_name, value)
        else:
            logging.error(f'ValueError wrong value - {value}')
            # raise ValueError(f'Wrong value - {value}')



class Range:
    def __init__(self, min_value, max_value):
        self.min_val = min_value
        self.max_val = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value is not None:
            if value > self.max_val or value < self.min_val:
                logging.error(f'ValueError wrong value - {value}')
                #raise ValueError(f'Wrong value - {value}')
            else:
                setattr(instance, self.param_name, value)


class Student:
    name = CheckName()
    last_name = CheckName()
    _test_mark = Range(0, 100)
    _control_mark = Range(2, 5)

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        #self.subjects = self._get_subjects()
        logging.info(f'Student {name} {last_name} created')

    def __repr__(self):
        return f'Student({self.name}, {self.last_name}, {self.subjects})'

    @staticmethod
    def _get_subjects():
        subjects = {}
        with open('subjects.csv', 'r', encoding='utf-8') as f:
            csv_read = csv.reader(f)
            for row in csv_read:
                row_ = ''.join(row) + ' - тесты'
                subjects[row_] = []
                row_ = ''.join(row) + ' - контрольные'
                subjects[row_] = []
        return subjects

    def get_test_average(self):
        average_val = {}
        for key, value in self.subjects.items():
            if 'тесты' in key:
                if len(value) > 0:
                    average_val[key] = sum(value) / len(value)
        return average_val

    def get_marks_average(self):
        sum_ = 0
        count_of_subj = 0
        for key, value in self.subjects.items():
            count_of_subj = len(value)
            if 'контрольные' in key:
                if len(value) > 0:
                    sum_ += sum(value)
        if not sum_ == 0:
            return sum_ / count_of_subj
        return 0

    def set_test_mark(self, subject_name, value):
        self._test_mark = value
        self.subjects[subject_name].append(self._test_mark)

    def set_control_mark(self, subject_name, value):
        self._control_mark = value
        self.subjects[subject_name].append(self._control_mark)



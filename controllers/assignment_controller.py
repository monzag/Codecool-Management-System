from models.assignment import Assignment


def get_assignments_to_table(student_index):
    '''
    '''
    table = []
    for assignment in Assignment.list_of_assignments:
        solution = []
        solution.append(assignment.name)
        solution.append(assignment.add_date)
        solution.append(assignment.deadline)
        solution.append(assignment.max_grade)
        solution.append(assignment.solutions[student_index].formated_grade)
        solution.append(assignment.solutions[student_index].formated_submit_date)

        table.append(solution)

    return table

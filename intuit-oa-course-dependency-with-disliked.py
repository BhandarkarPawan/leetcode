# Do not remove these imports. You may add others if you wish.
import sys
from collections import defaultdict, deque

# Args:
#   disliked: a string, the course you want to avoid taking
#   prereqs: a list of list of strings, each list is a course pair
#            The first course must be taken before the second can be taken
#            ex: [["Algorithms", "AI"], ...] -> Take Algorithms before taking AI
# Returns:
#   an int, the number of courses you can take before taking disliked


def count_courses(disliked, prereqs):
    # Your code goes here
    # NOTE: You may use print statements for debugging purposes, but you may
    #       need to remove them for the tests to pass.

    # create a mapping of courses and dependencies
    dependency_map = defaultdict(lambda: [])
    unique_courses = set({})

    for prereq, course in prereqs:
        dependency_map[prereq].append(course)

        unique_courses.add(course)
        unique_courses.add(prereq)

    visited = set({})
    dependency_queue = deque(dependency_map[disliked])
    visited.update(dependency_queue)

    while len(dependency_queue):
        course = dependency_queue.popleft()
        for dependent_course in dependency_map[course]:
            if dependent_course not in visited:
                visited.add(dependent_course)
                dependency_queue.append(dependent_course)

    courses_we_can_take = len(unique_courses) - len(visited) - 1
    return courses_we_can_take

# DO NOT MODIFY BELOW THIS LINE


def main():
    break_line = False
    disliked = ""
    prereqs = []

    for line in sys.stdin:
        line = line.strip()
        if len(line) == 0:
            break_line = True
            continue

        if break_line:
            prereqs.append(line.split(","))
        else:
            disliked = line.split(",")[0]

    print(count_courses(disliked, prereqs))


main()

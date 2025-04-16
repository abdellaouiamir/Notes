def count_marketers(job_titles):
    count = 0
    for job in job_titles:
        if job == "marketer":
            count += 1
    return count
def last_work_experience(work_experiences):
    return work_experiences[-1]
if __name__ == "__main__":
    count = count_marketers(['programmer', 'marketer', 'doctor', 'marketer'])
    print(count)
    print(last_work_experience(["pro", "eifj", "eifjaemr"])) 

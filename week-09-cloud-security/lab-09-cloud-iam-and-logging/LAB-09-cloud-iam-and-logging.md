::: title-page
# Lab 09 — Cloud identity, logs, and a small bill

**Course:** Maxim Nyansa Cybersecurity Bootcamp, Ghana  
**Trainee:** James Ackah Blay · Aiyinasi, Ghana  
**Week:** 9 — Cloud computing and cloud security  
**Estimated time:** 5 hours  
**Difficulty:** Advanced. You may stop after the paper exercise. Opening an account is optional and comes after a budget alarm.

::: tutor
**Tutor note.** Cost comes before curiosity. A free tier is not a promise that every click is free. If you open an account, set a budget alarm at 1 USD, use one region, and delete what you create. Practical platform for the risk register and the shared-responsibility matrix: https://grclab.purplecop.io/lab . This guide does not describe that site.
:::
:::

## 1. Learning objectives

| Objective | Job skill |
| --- | --- |
| Compare public, private, and hybrid without slogans | Architecture conversations with a customer |
| Say who patches the guest on IaaS | Shared responsibility, checked against the provider page |
| Read identity and trail configuration | Cloud SOC: IAM and CloudTrail, or the paper equivalent |
| Keep a bucket private, and check that it is | The misconfiguration that becomes a breach story |

## 2. Prerequisites and setup

Week 4 scoring. The AWS CLI only if you choose to open an account: `aws --version`. A budget alarm is Task 1, before any bucket.

If you do not want an account, write `account_opened=no` in `cloud-notes.md` and finish Tasks 3 and 4 on paper. That still meets the lab.

## 3. Scenario

A school office wants mail in a public SaaS product and is asking whether the Wazuh server should move "to the cloud" too. You will separate the two decisions, name the risks, and, if you touch AWS, prove you can see who you are logged in as and whether a bucket is public.

## 4. Tasks

### Task 1 — Money first, if you use AWS

In the billing console, create a budget alarm at 1 USD. Record the date. Then:

```bash
aws sts get-caller-identity
```

::: checkpoint
**You should now see** an account id and an ARN that belong to the lab user, not the root user. If the command shows root, stop and create an IAM user with access keys you can delete. Do not put those keys in git.
:::

### Task 2 — Identity and the trail

```bash
aws iam list-users --query 'Users[].UserName' --output text
aws iam list-mfa-devices --user-name YOUR_LAB_USER
aws cloudtrail describe-trails --query 'trailList[].{Name:Name,IsMultiRegion:IsMultiRegionTrail}'
```

Replace `YOUR_LAB_USER`. If MFA is empty, the finding is "MFA not on for this user". Do not mark the checklist `met`.

### Task 3 — A private bucket, then tear it down

Skip this if you have no account. Bucket names are global. Pick a long unique name.

```bash
aws s3api create-bucket --bucket YOUR-UNIQUE-NAME --region us-east-1
aws s3api put-public-access-block --bucket YOUR-UNIQUE-NAME --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
aws s3api get-public-access-block --bucket YOUR-UNIQUE-NAME
aws s3 rb s3://YOUR-UNIQUE-NAME
```

`us-east-1` does not need a location constraint. If you choose another region, add the location constraint the CLI asks for, and do not also leave a bucket in the first region.

::: checkpoint
**You should now see** all four public-access settings true, then a successful delete. If delete fails, the bucket is not empty or the name is wrong. Do not leave it.
:::

### Task 4 — Paper models and the risk register

Fill `../cloud-deployment-comparison/comparison.md`, `../shared-responsibility/responsibility-matrix.csv` for the service you actually mean, and `../cloud-risk-register/cloud-risk-register.csv` with `example=no` on your rows. Confirm the provider's current shared-responsibility page before you submit the matrix as if it were theirs.

Use the GRC Lab for the risk register exercise and save your export beside the CSV.

## 5. Troubleshooting

| What you see | What it means |
| --- | --- |
| `Unable to locate credentials` | No keys, or the wrong profile. `aws configure list` |
| `BucketAlreadyExists` | The name is taken worldwide. Choose another. Do not try to "claim" someone else's |
| Bill preview is not zero | Stop. Delete the bucket. Check for an Elastic IP or a running VM you did not mean to start |
| MFA command errors | The user name is wrong, or you are still on root |

## 6. Stretch task

Turn on CloudTrail in one region only if the budget alarm exists, note the trail bucket, then delete the trail if you will not use it after the bootcamp. Write the monthly cost you saw in the pricing page before you enabled it. If you cannot find a price, do not enable it.

## 7. Evidence

- `account_opened` yes or no.
- Budget alarm date, if yes.
- Command output for identity, MFA, and the public-access block, or "not run".
- Risk register rows that are yours.
- GRC Lab export, or a blank line.

## 8. Reflection

1. What stays yours if the mailbox is SaaS?
2. Why did the bucket task end with a delete?
3. What would you refuse to put in a public bucket even "for a minute"?

## 9. Interview questions

1. Who patches the guest operating system in the usual IaaS model?
2. What does CloudTrail give you that a single server's log does not?
3. How do you check whether an S3 bucket is blocked from public access?
4. What is the first control you want on a cloud admin user?

## 10. Grading rubric

| Criterion | Exceeds | Meets | Not yet |
| --- | --- | --- | --- |
| Cost | You deleted what you created and can say the budget level | Account decision is explicit | A resource left running with no note |
| Identity | MFA gap or MFA evidence is real | `get-caller-identity` saved, or paper path is honest | Root keys in the repository |
| Risk | Your cloud risks have owners | Example rows kept separate | Example scores submitted as a tenant you do not have |

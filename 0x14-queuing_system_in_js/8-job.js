/*
create a function named createPushNotificationsJobs:

- It takes into argument jobs (array of objects), and queue (Kue queue)
- If jobs is not an array, it should throw an Error with message: Jobs is not an array
- For each job in jobs, create a job in the queue push_notification_code_3
- When a job is created, it should log to the console Notification job created: JOB_ID
- When a job is complete, it should log to the console Notification job JOB_ID completed
- When a job is failed, it should log to the console Notification job JOB_ID failed: ERROR
- When a job is making progress, it should log to the console Notification job JOB_ID PERCENT% complete

*/


function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  for (const jobData of jobs) {
    const job = queue.create('push_notification_code_3', jobData)
      .save((error) => {
        if (!error) console.log(`Notification job created: ${job.id}`);
      });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (error) => {
      console.log(`Notification job ${job.id} failed: ${error}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  }
}

module.exports = createPushNotificationsJobs;

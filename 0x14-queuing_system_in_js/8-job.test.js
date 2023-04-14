/*

  - Import the function createPushNotificationsJobs
  - Create a queue with Kue
  - Write a test suite for the createPushNotificationsJobs function:
    - Use queue.testMode to validate which jobs are inside the queue
    - etc.

Requirements:

  - Make sure to enter the test mode without processing the jobs before executing the tests
  - Make sure to clear the queue and exit the test mode after executing the tests
*/

import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should create a job for each device', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code');
    expect(queue.testMode.jobs[0].data).to.deep.equal(list[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code');
    expect(queue.testMode.jobs[1].data).to.deep.equal(list[1]);
  });
});

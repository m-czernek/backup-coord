# Backup Coordinator

A Slack workflow trigger to remind the team who the backup coordinator is this month

## Deploying the project

The project is built as an RPM in https://build.opensuse.org/package/show/home:mczernek/backup-coord.

Because the project requires a Slack webhook URL (which should stay secret), a built container is not available.
Build the container locally on the machine where you want to deploy the project:

```shell
git clone https://github.com/m-czernek/backup-coord.git
cd backup-coord
containers/build.sh
docker run -d --name backup-coord localhost/backup-coord
```

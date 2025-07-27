FROM registry.suse.com/bci/bci-base:15.7

ARG webhook
ENV slack_webhook_url=$webhook

RUN zypper addrepo https://download.opensuse.org/repositories/home:mczernek/15.6/home:mczernek.repo && \
    zypper --non-interactive --gpg-auto-import-keys ref && zypper --non-interactive up && \
    zypper --gpg-auto-import-keys --non-interactive install --auto-agree-with-licenses --force-resolution \
        python311 \
        python311-backup-coord \
        cron

# set up cron
RUN echo '0 0 1 * * backup-coord >/proc/1/fd/1 2>/proc/1/fd/2' > /etc/cron.d/backup-coord && \
    crontab /etc/cron.d/backup-coord

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["cron", "-n"]
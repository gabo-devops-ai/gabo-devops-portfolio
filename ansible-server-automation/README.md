# Ansible Server Automation

Playbooks to configure a minimal web server and deploy a demo app.

## Files
- `inventory.ini` — example inventory.
- `site.yml` — main playbook.
- `roles/web/tasks/main.yml` — installs and configures Nginx.

## Run
```bash
ansible-playbook -i inventory.ini site.yml
```
rs.initiate();
rs.reconfig({ _id: 'rs0', version: 1, members: [{ _id: 0, host : 'bifrost_db:27017' }]}, { force: true });
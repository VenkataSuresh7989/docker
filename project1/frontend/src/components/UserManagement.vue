<template>
  <div class="container">
    <h2>User Management System</h2>

    <!-- User Form -->
    <div class="card">
      <h3>{{ editMode ? 'Edit User' : 'Add New User' }}</h3>
      <form @submit.prevent="saveUser">
        <div class="form-group">
          <label>Name:</label>
          <input v-model="form.name" type="text" placeholder="Enter name" required />
        </div>

        <div class="form-group">
          <label>Email:</label>
          <input v-model="form.email" type="email" placeholder="Enter email" required />
        </div>

        <div class="form-group">
          <label>Gender:</label>
          <select v-model="form.gender" required>
            <option value="" disabled>Select Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Others">Others</option>
          </select>
        </div>

        <button type="submit" class="btn btn-submit">
          {{ editMode ? 'Update User' : 'Add User' }}
        </button>
        <button v-if="editMode" type="button" class="btn btn-cancel" @click="resetForm">
          Cancel
        </button>
      </form>
    </div>

    <!-- User Table -->
    <div class="card">
      <h3>User List</h3>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Gender</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id">
            <td>{{ user.id }}</td>
            <td>{{ user.name }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.gender }}</td>
            <td>
              <button class="btn btn-edit" @click="editUser(user)">Edit</button>
              <button class="btn btn-delete" @click="deleteUser(user.id)">Delete</button>
            </td>
          </tr>
          <tr v-if="users.length === 0">
            <td colspan="5" style="text-align: center;">No users found.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://localhost:8000/users';

export default {
  data() {
    return {
      users: [],
      editMode: false,
      selectedUserId: null,
      form: {
        name: '',
        email: '',
        gender: ''
      }
    };
  },
  mounted() {
    this.fetchUsers();
  },
  methods: {
    // Fetch all records
    async fetchUsers() {
      try {
        const response = await axios.get(API_URL);
        this.users = response.data;
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },

    // Save or Update record
    async saveUser() {
      try {
        if (this.editMode) {
          await axios.put(`${API_URL}/${this.selectedUserId}`, this.form);
        } else {
          await axios.post(API_URL, this.form);
        }
        this.resetForm();
        this.fetchUsers();
      } catch (error) {
        alert(error.response?.data?.detail || 'An error occurred');
      }
    },

    // Populate form for editing
    editUser(user) {
      this.editMode = true;
      this.selectedUserId = user.id;
      this.form = { name: user.name, email: user.email, gender: user.gender };
    },

    // Delete record
    async deleteUser(id) {
      if (confirm('Are you sure you want to delete this user?')) {
        try {
          await axios.delete(`${API_URL}/${id}`);
          this.fetchUsers();
        } catch (error) {
          console.error('Error deleting user:', error);
        }
      }
    },

    // Reset Form fields
    resetForm() {
      this.editMode = false;
      this.selectedUserId = null;
      this.form = { name: '', email: '', gender: '' };
    }
  }
};
</script>

<style scoped>
.container { max-width: 800px; margin: 0 auto; }
.card { background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
.form-group { margin-bottom: 15px; }
.form-group label { display: block; margin-bottom: 5px; font-weight: bold; }
.form-group input, .form-group select { width: 100%; padding: 8px; box-sizing: border-box; }
.btn { padding: 8px 12px; border: none; border-radius: 4px; cursor: pointer; margin-right: 5px; }
.btn-submit { background-color: #28a745; color: white; }
.btn-cancel { background-color: #6c757d; color: white; }
.btn-edit { background-color: #ffc107; color: black; }
.btn-delete { background-color: #dc3545; color: white; }
table { width: 100%; border-collapse: collapse; }
th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
th { background-color: #f2f2f2; }
</style>
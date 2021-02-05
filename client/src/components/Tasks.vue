<template>
  <v-container class="grey lighten-5">
    <v-row>
      <v-col
        align="start"
        class="grey lighten-5 text-center"
        style="height: 550px;"
      >
        <v-card raised style="display: block">
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-4">NFOV Camera</div>
              <v-list-item-title class="headline mb-1">Camera Tasking</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-card-title>
              <v-spacer></v-spacer>
              <v-spacer></v-spacer>
              <v-text-field
                  v-model="search"
                  append-icon="mdi-magnify"
                  label="Search"
                  single-line
                  hide-details
              ></v-text-field>
          </v-card-title>
          <v-data-table
            v-model="selected"
            :headers="headers"
            :items="tasks"
            :single-select="true"
            :search="search"
            item-key="name"
            class="elevation-1"
            height="300px"
          >
           <template v-slot:top>
             <v-toolbar flat color="white">
               <v-toolbar-title>Task List</v-toolbar-title>
               <v-divider
                 class="mx-4"
                 inset
                 vertical
               ></v-divider>
               <v-spacer></v-spacer>
               <v-dialog v-model="dialog" max-width="500px">
                 <template v-slot:activator="{ on }">
                   <v-btn color="primary" dark class="mb-2" v-on="on">New Task</v-btn>
                 </template>
                 <v-card>
                   <v-card-title>
                     <span class="headline">{{ formTitle }}</span>
                   </v-card-title>
                   <v-card-text>
                     <v-container>
                         <v-row>
                           <v-col cols="12" sm="6" md="4">
                             <v-text-field
                               v-model="editedItem.name"
                               label="Task Name">
                             </v-text-field>
                           </v-col>
                           <v-col cols="12" sm="6" md="4">
                             <v-text-field
                               v-model="editedItem.priority"
                               label="Priority">
                             </v-text-field>
                           </v-col>
                         </v-row>
                         <v-row>
                           <v-col cols="12" sm="6" md="4">
                             <v-text-field
                               v-model="editedItem.long"
                               label="Longitude">
                             </v-text-field>
                           </v-col>
                           <v-col cols="12" sm="6" md="4">
                             <v-text-field
                               v-model="editedItem.lat"
                               label="Latitude">
                             </v-text-field>
                           </v-col>
                         </v-row>
                     </v-container>
                   </v-card-text>
                   <v-card-actions>
                     <v-spacer></v-spacer>
                     <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                     <v-btn color="blue darken-1" text @click="save">Save</v-btn>
                   </v-card-actions>
                 </v-card>
               </v-dialog>
             </v-toolbar>
           </template>
           <template v-slot:item.actions="{ item }">
             <v-tooltip left>
               <template v-slot:activator="{ on }">
                 <v-icon v-on="on"
                   small
                   class="mr-2"
                   @click="editItem(item)"
                 >
                   mdi-pencil
                 </v-icon>
               </template>
               <span>Edit task</span>
             </v-tooltip>
             <v-tooltip right>
               <template v-slot:activator="{ on }">
                 <v-icon v-on="on"
                   small
                   class="mr-2"
                   @click="deleteItem(item)"
                 >
                   mdi-delete
                 </v-icon>
               </template>
               <span>Delete task</span>
             </v-tooltip>
           </template>
           <template v-slot:no-data>
             <v-btn color="primary" @click="initialize">Reset</v-btn>
           </template>
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
/* eslint-disable no-unused-expressions, no-alert, no-console */
// import axios from 'axios';

export default {
  data() {
    return {
      dialog: false,
      search: '',
      selected: [],
      headers: [
        {
          text: 'Name',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        { text: 'Priority', value: 'priority' },
        { text: 'Longitude', value: 'long' },
        { text: 'Latitude', value: 'lat' },
        { text: 'Actions', value: 'actions', sortable: false },
      ],
      tasks: [],
      editedIndex: -1,
      editedItem: {
        name: '',
        priority: 'low',
        long: 0,
        lat: 0,
      },
      defaultItem: {
        name: '',
        priority: 'low',
        long: 0,
        lat: 0,
      },
    };
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'New Task' : 'Edit Task';
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
  },

  created() {
    this.initialize();
  },

  methods: {
    initialize() {
      this.tasks = [
        {
          name: 'Task1',
          priority: 'med',
          long: '110.32',
          lat: 32.226,
        },
        {
          name: 'Task2',
          priority: 'high',
          long: '67.32',
          lat: 32.226,
        },
        {
          name: 'Task3',
          priority: 'low',
          long: '111.32',
          lat: 97.226,
        },
      ];
    },

    editItem(item) {
      this.editedIndex = this.tasks.indexOf(item);
      this.editedItem = { ...item };
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.tasks.indexOf(item);
      // esline-disable-next-line
      window.confirm('Are you sure you want to delete this item?') && this.tasks.splice(index, 1);
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = { ...this.defaultItem };
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.tasks[this.editedIndex], this.editedItem);
      } else {
        this.tasks.push(this.editItem);
      }
      this.close();
    },
  },
};

</script>

<style scoped>
  .databox {
    max-width: 600px;
    max-height: 600px;
    margin: auto;
  }
</style>

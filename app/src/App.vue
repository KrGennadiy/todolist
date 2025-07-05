<template>
	<table class="table">
		<tr>
			<td colspan="2">
				<h1 class="head">{{ mainHeader }}</h1>
			</td>
		</tr>
		<tr v-for="(task, index) in tasks">
			<td>{{ task.text }}</td>
			<td><button @click="deleteTask(task.id)"> удалить </button> </td>
		</tr>
		<tr>
			<td><input type="text" v-model.trim="textTask" placeholder="задача"
					@keyup.enter="pushToBack(), clearInput()">
			</td>
			<td><button id="mainButton" v-show="textTask != ''" @click="pushToBack(),
				clearInput()">Добавить</button>
			</td>
		</tr>
	</table>
</template>

<script>
import axios from 'axios'
const api = axios.create({
	baseURL: 'http://localhost:8088'
})


export default {
	data() {
		return {
			mainHeader: 'to-do list',
			tasks: [],
			textTask: ''
		}
	},
	mounted() {
		this.pullFromBack();
		setInterval(this.pullFromBack, 500);
	},
	methods: {
		pullFromBack() {
			api.post('/pullTask')
				.then(response => { this.tasks = response.data }, console.log(this.tasks))
				.catch(error => console.error(error))
		},
		pushToBack() {
			api.post('/pushTask', { text: this.textTask })
				.then(response => console.log(response.text))
				.catch(error => console.error(error))

		},
		clearInput() {
			this.textTask = ''
		},
		deleteTask(index) {
			api.post('/deleteTask', { id: index }, {_method: 'delete'}
			)
				.then(response => console.log(response.data))
				.catch(error => console.error(error))
		}
	}
}
</script>

<style scoped>
h1 {
	color: rgb(49, 166, 63);
	font-weight: lighter;
}

.head {
	text-align: center;
}

.table {
	margin: auto;

}

button {
	width: 100px;
}
</style>

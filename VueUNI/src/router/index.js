import { createRouter, createWebHistory } from 'vue-router'
import Page  from '../views/Page.vue'
import Password  from '../views/PasswordChange.vue'
import PageAuth from '../views/PageAuth.vue'
import Login  from '../views/Login.vue'
import Profile  from '../views/Profile.vue'
import Notification  from '../views/Notification.vue'
import Chat  from '../views/Chat.vue'
import Course  from '../views/Course.vue'
import PersonsCourse  from '../views/PersonsCourse.vue'
import AddMaterials  from '../views/AddMaterials.vue'
import EditUser  from '../views/EditUser.vue'
import EditMaterials  from '../views/EditMaterials.vue'
import Notallowed  from '../views/NotAllowed.vue'
import UnenrolledCourse  from '../views/UnenrolledCourse.vue'
import SetKey  from '../views/SetKey.vue'
import Blog  from '../views/Blog.vue'
import CreatePost  from '../views/CreatePost.vue'
import EditPost  from '../views/EditPost.vue'
import Colleges  from '../views/Colleges.vue'
import CourseFromCollege  from '../views/CoursefrmCollege.vue'
import Practices  from '../views/Practices.vue'
import ProblemsSolutions  from '../views/AddProblemsSolutions.vue'
import Test  from '../views/Test.vue'
import Friendship  from '../views/Friendship.vue'
import Group  from '../views/CreateGroup.vue'
import AddUser  from '../views/AddUserGroup.vue'
import Report  from '../views/Report.vue'
import CreateReport  from '../views/CreateReport.vue'
import Forum  from '../views/Forum.vue'
import ForumList  from '../views/ForumsList.vue'
import My from '../views/Calendar.vue'
import CreateEvent from '../views/CreateEvent.vue'
import EventDescription from '../views/EventsDescription.vue'
import EditEvent from '../views/EditEvent.vue'
import Qualifications from '../views/Qualifications.vue'
import GroupDetails from '../views/GroupDetails.vue'
import Certificates from '../views/Certificates.vue'
import Resumes from '../views/Resumes.vue'
import CreateUser from '../views/CreateUser.vue'
import BeforeTest from '../views/BeforeTest.vue'
import CreateCourse from '../views/CreateCourse.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'page',
      component: Page
    },
    {
      path: '/password',
      name: 'password',
      component: Password
    },
    {
      path: '/notallowed',
      name: 'notAllowed',
      component: Notallowed
    },
    {
      path: '/course/create',
      name: 'createcourse',
      component: CreateCourse
    },
    {
      path: '/my',
      name: 'calendar',
      component: My
    },
    {
      path: '/my',
      name: 'calendar',
      component: My
    },
    {
      path: '/forums',
      name: 'forums',
      component: ForumList
    },
    {
      path: '/resume',
      name: 'resumes',
      component: Resumes
    },
    {
      path: '/my/create-event',
      name: 'createevent',
      component: CreateEvent
    },
    {
      path: '/my/event/:id',
      name: 'editevent',
      component: EditEvent
    },
    {
      path: '/my/event',
      name: 'eventdescription',
      component: EventDescription
    },
    
    {
      path: '/main',
      name: 'pageauth',
      component: PageAuth
    },
    {
      path: '/friendship',
      name: 'friendship',
      component: Friendship
    },
    {
      path: '/signup',
      name: 'signup',
      component: CreateUser
    },
    {
      path: '/course/:id',
      name: 'course',
      component: Course
    },
    {
      path: '/course/:id/qualifications',
      name: 'qualification',
      component: Qualifications
    },
    {
      path: '/course/forum/:id',
      name: 'forum',
      component: Forum
    },
    {
      path: '/course/:id/practices',
      name: 'practices',
      component: Practices
    },
    {
      path: '/course/:id/practices/:pk/test',
      name: 'beforetest',
      component: BeforeTest
    },
    {
      path: '/course/:id/practices/:pk/test/attempt',
      name: 'test',
      component: Test
    },
    {
      path: '/course/:id/practices/:pk',
      name: 'problemsolutions',
      component: ProblemsSolutions
    },
    {
      path: '/course/:id/setkey/',
      name: 'setKey',
      component: SetKey
    },
    {
      path: '/course/:id/enroll',
      name: 'enrollCourse',
      component: UnenrolledCourse
    },
    {
      path: '/course/:id/participants',
      name: 'personsCourse',
      component: PersonsCourse
    },
    {
      path: '/course/:id/participants/report/:pk',
      name: 'createreport',
      component: CreateReport
    },
    {
      path: '/course/:id/edit/:pk',
      name: 'editMaterials',
      component: EditMaterials
    },
    {
      path: '/course/:id/add',
      name: 'addMaterials',
      component: AddMaterials,
    },
    {
      path: '/chat',
      name: 'chat',
      component: Chat
    },
    {
      path: '/certificates',
      name: 'certificate',
      component: Certificates
    },
    {
      path: '/group/:id',
      name: 'groupdetails',
      component: GroupDetails
    },
    {
      path: '/groups',
      name: 'groups',
      component: Group
    },
    {
      path: '/report',
      name: 'report',
      component: Report
    },
    {
      path: '/addUser/:id',
      name: 'adduser',
      component: AddUser
    },
    {
      path: '/notifications',
      name: 'notification',
      component: Notification
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: Profile
    },
    {
      path: '/blog/:id',
      name: 'blog',
      component: Blog
    },
    
    {
      path: '/blog/:id/post',
      name: 'blogpost',
      component: CreatePost
    },
    {
      path: '/colleges',
      name: 'colleges',
      component: Colleges
    },
    {
      path: '/colleges/:id',
      name: 'college',
      component: CourseFromCollege
    },
    {
      path: '/blog/:id/post/:pk',
      name: 'editPost',
      component: EditPost
    },
    {
      path: '/profile/:id/edit',
      name: 'profileedit',
      component: EditUser
    },

    {
      path: '/login',
      name: 'login',
      component: Login
    },
    
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
    }
  ]
})

export default router

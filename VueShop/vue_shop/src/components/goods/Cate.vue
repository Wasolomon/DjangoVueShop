<template>
    <div>
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>商品管理</el-breadcrumb-item>
        <el-breadcrumb-item>商品列表</el-breadcrumb-item>
      </el-breadcrumb>
      <el-card>
        <el-row>
          <el-col>
            <el-button type="primary" @click="showAddCateDialog">添加分类</el-button>
          </el-col>
        </el-row>
        <tree-table :data="cateList" :columns="columns" :selection-type="false" :expand-type="false" show-index border class="treeTable">
          <template slot="isOk" slot-scope="scope">
            <i class="el-icon-success" v-if="scope.row.deleted === false" style="color: lightgreen;"></i>
            <i class="el-icon-error" v-else style="color: red;"></i>
          </template>
          <template slot="order" slot-scope="scope">
            <el-tag size="mini" v-if="scope.row.level === '1'">一级</el-tag>
            <el-tag type="success" size="mini" v-else-if="scope.row.level === '2'">二级</el-tag>
            <el-tag type="warning" size="mini" v-else>三级</el-tag>
          </template>
          <template slot="opt" slot-scope="">
            <el-button type="primary" icon="el-icon-edit" size="mini">编辑</el-button>
            <el-button type="danger" icon="el-icon-delete" size="mini">删除</el-button>
          </template>
        </tree-table>
         <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="queryInfo.page"
          :page-sizes="[3, 5, 10]"
          :page-size="queryInfo.size"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total">
        </el-pagination>
      </el-card>
      <el-dialog
        title="添加分类"
        :visible.sync="addCateDialogVisible"
        width="50%">
        <el-form :model="addCateForm" :rules="addCateFormRules" ref="addCateRuleForm" label-width="100px">
          <el-form-item label="分类名称:" prop="name">
            <el-input v-model="addCateForm.name"></el-input>
          </el-form-item>
          <el-form-item label="父级分类:">
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="addCateDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="addCateDialogVisible = false">确 定</el-button>
        </span>
      </el-dialog>
    </div>
</template>

<script>
export default {
  data() {
    return {
      queryInfo: {
        search: '0',
        page: 1,
        size: 5
      },
      total: 0,
      cateList: [],
      columns: [
        {
          label: '分类名称',
          prop: 'name'
        },
        {
          label: '是否有效',
          prop: 'deleted',
          type: 'template',
          template: 'isOk'
        },
        {
          label: '排序',
          type: 'template',
          template: 'order'
        },
        {
          label: '操作',
          type: 'template',
          template: 'opt'
        }
      ],
      addCateDialogVisible: false,
      addCateForm: {
        name: '',
        pid: 0,
        level: 0
      },
      addCateFormRules: {
        name: [
          { required: true, message: '请输入用户名称', trigger: 'blur' }
        ]
      },
      parentCateList: []
    }
  },
  created() {
    this.getCateList()
  },
  methods: {
    async getCateList() {
      const { data: res } = await this.$http.get('/account/category/1/', { params: this.queryInfo })
      if (res.code !== 200) {
        return this.$message.error('获取商品分类失败')
      }
      console.log(res.data)
      this.cateList = res.data.children
      this.total = res.data.children.length
    },
    handleSizeChange(newSize) {
      this.queryInfo.size = newSize
      this.getCateList()
    },
    handleCurrentChange(newPage) {
      this.queryInfo.page = newPage
      this.getCateList()
    },
    showAddCateDialog() {
      this.getParentCateList()
      this.addCateDialogVisible = true
    },
    async getParentCateList() {
      const { data: res } = await this.$http.get('/account/category/2/', { params: { type: 2 } })
      if (res.code !== 200) {
        return this.$message.error('获取父级分类数据失败')
      }
      console.log(res.data)
      this.parentCateList = res.data
    }
  }
}
</script>

<style lang="less" scoped>
  .treeTable {
    margin-top: 15px
  }
</style>

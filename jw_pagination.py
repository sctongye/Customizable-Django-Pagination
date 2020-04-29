# -*- coding: utf-8 -*-
"""
Created by @南卡统爷 on 4/28/20 3:43 PM.
"""
__author__ = '@SCTongYe'


from django.utils.safestring import mark_safe


class JWPagination():

    def __init__(self, page_number, total_customer_count, page_linkpath, per_page_number=10, side_page_number=2):
        # 自定义分页
        # 需要的参数：
            # 当前页码 page_number = request.GET.get('page', 1)
            # 总数据量 total_customer_count = customer_objs = Customer.objects.all().count()
            # 每页显示数据个数 per_page_number = 10
            # 页码栏正中页数左右各显示几个页码 side_page_number = 2
            # 部署页面的文件名 page_linkpath = 'customers'

        try:
            page_number = int(page_number)
        except Exception:
            page_number = 1
        if page_number < 1:
            page_number = 1


        self.total_customer_count = total_customer_count
        self.page_linkpath = page_linkpath
        self.per_page_number = per_page_number

        # 计算总数据量，定义单页显示数据个数，相除得总页数，如果有余数，总页数等于商加一
        _q, _r = divmod(total_customer_count, per_page_number)

        if _r:
            total_page_count = _q + 1
        else:
            total_page_count = _q

        self.total_page_count = total_page_count

        if page_number > total_page_count:
            page_number = total_page_count

        self.page_number = page_number

        # 正中间显示页面

        start_page_number = page_number - side_page_number
        end_page_number = page_number + side_page_number

        if start_page_number < 1:
            start_page_number = 1
            end_page_number = side_page_number * 2 + 1
        if end_page_number > total_page_count:

            start_page_number = total_page_count - (side_page_number * 2 + 1) + 1
            if start_page_number < 1:
                start_page_number = 1

            end_page_number = total_page_count


        self.start_page_number = start_page_number
        self.end_page_number = end_page_number
        self.total_page_count_range = range(start_page_number, end_page_number + 1)


    @property
    def data_range_start(self):
        return (self.page_number - 1) * self.per_page_number


    @property
    def data_range_end(self):
        return self.page_number * self.per_page_number


    @property
    def pagination_html(self):

        pagination_html = ''

        page_pre_html = '<nav aria-label="Page navigation example"><ul class="pagination">'
        if self.start_page_number > 1:
            page_pre_html = '<nav aria-label="Page navigation example"><ul class="pagination"><li><a href="{0}?page={1}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(self.page_linkpath, self.page_number-1)

        pagination_html += page_pre_html

        for i in self.total_page_count_range:
            if i == self.page_number:
                pagination_html += '<li class="active" class="page-item"><a class="page-link" href="{0}?page={1}">{2}</a></li>'.format(self.page_linkpath, i, i)
            else:
                pagination_html += '<li class="page-item"><a class="page-link" href="{0}?page={1}">{2}</a></li>'.format(self.page_linkpath, i, i)

        page_next_html = '</ul></nav>'
        if self.end_page_number < self.total_page_count:

            page_next_html = '<li><a href="{0}?page={1}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li></ul></nav>'.format(self.page_linkpath, self.page_number+1)

        pagination_html += page_next_html

        return mark_safe(pagination_html)
